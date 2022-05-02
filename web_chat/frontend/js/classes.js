class Sender {
	payload;

	constructor(api_url) {
		this.api_url = api_url
	}

	prepare_message(id, date, message_text) {
		let message = {
			"_id": id, "date": date, "content": message_text
		}
		this.payload = {
			method: "PUT", body: JSON.stringify(message), headers: {
				"Access-Control-Allow-Origin": "*", "Content-Type": "application/json",
			}
		}
	}

	send_put_request(prefix) {
		fetch(this.api_url + prefix, this.payload).then(() => {
		});
	}

	async send_get_request(prefix) {
		const response = await fetch(this.api_url + prefix)
		return response.json();
	}

}


class Message extends Sender {
	id;
	message;
	date;

	constructor(input_box_name, api_url) {
		super(api_url);
		this.input_box_name = input_box_name
	}

	async get_id() {
		this.id = ((await this.send_get_request("posts/get_last_id"))["last_id"]) + 1
	}

	get_message() {
		this.message = document.querySelector(`${this.input_box_name}`).value;
	}

	get_date() {
		let current_date = new Date().toLocaleDateString();
		let current_time = new Date().toLocaleTimeString('en-US', {
			hour12: false, hour: "numeric", minute: "numeric", second: "numeric"
		});
		this.date = current_date + " " + current_time;
	}


	clean_input_box() {
		document.querySelector(`${this.input_box_name}`).value = "";
	}

	async send_message() {
		await this.get_id()
		this.get_message()
		this.get_date()
		this.prepare_message(this.id, this.date, this.message)
		this.send_put_request("posts/new")
		this.clean_input_box()
	}
}


class Renderer extends Message {
	constructor() {
		super();
	}

	async create_element_with_class(type, className) {
		const element = document.createElement(type);
		element.className = className;
		return element;
	}

	async create_wrapper_divs() {
		const new_post = await this.create_element_with_class("div", "post");
		const new_post_header = await this.create_element_with_class("div", "post-header");
		return [new_post, new_post_header];
	}

	async create_data_divs() {
		const new_post_number = await this.create_element_with_class("div", "post-number");
		const new_post_date = await this.create_element_with_class("div", "post-date");
		const new_post_contents = await this.create_element_with_class("div", "post-contents");
		return [new_post_number, new_post_date, new_post_contents];
	}

	async build_post(wrapper_divs, filled_divs) {
		const posts = document.querySelector("#posts")

		const post = posts.appendChild(wrapper_divs[0])
		const post_header = post.appendChild(wrapper_divs[1])
		post_header.appendChild(filled_divs[0]);
		post_header.appendChild(filled_divs[1]);
		post.appendChild(filled_divs[2]);
		return post
	}

	async format_id(id) {
		return ("#" + ((id.toString()).padStart(6, "0").match(/.{1,2}/g))).replace(new RegExp(",", "g"), "-");
	}

	async fill_divs(data_divs, array_of_data) {
		if (data_divs.length !== array_of_data.length) {
			throw "There are fewer data_divs than data for them!"
		}
		for (let i = 0; i < data_divs.length; i++) {
			data_divs[i].innerHTML += array_of_data[i];
		}
		return data_divs;
	}

	async remove_all_posts() {
		const posts = document.querySelector("#posts");
		posts.innerHTML = "";
	}

	async render_all_posts() {
		let posts = ((await message.send_get_request("posts/get_all"))["posts"]).reverse();
		if (posts.length === 0) {
			//	do nothing
		} else {
			for (let i = 0; i < posts.length; i++) {
				const wrapper_divs = await this.create_wrapper_divs()
				const filled_divs = await this.fill_divs(await this.create_data_divs(), [await this.format_id(posts[i]["_id"]), posts[i]["date"], posts[i]["content"]]);
				await this.build_post(wrapper_divs, filled_divs)
			}
		}
	}
}
