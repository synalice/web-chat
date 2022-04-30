class Sender {

	constructor(api_url) {
		this.api_url = api_url
	}

	payload;

	prepare_message(id, date, message_text) {
		let message = {
			"id": id, "date": date, "content": message_text
		}
		this.payload = {
			method: "PUT", body: JSON.stringify(message), headers: {
				"Access-Control-Allow-Origin": "*", "Content-Type": "application/json",
			}
		}
	}


	send_post_request() {
		fetch(this.api_url, this.payload).then(() => {
		});
	}

}


class Message extends Sender {

	constructor(input_box_name, api_url) {
		super(api_url);
		this.input_box_name = input_box_name
	}

	formatted_id;
	unformatted_id;
	message;
	date;

	get_id() {
		let last_post = (document.getElementsByClassName("post"))[0]
		this.unformatted_id = last_post.getElementsByClassName("post-header")[0]
			.getElementsByClassName("post-number")[0].innerHTML

	}

	format_id() {
		this.formatted_id = parseInt((this.unformatted_id.slice(1)).split("-").join(""))
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

	send_message() {
		this.get_id()
		this.format_id()
		this.get_message()
		this.get_date()
		this.prepare_message(this.formatted_id, this.date, this.message)
		this.send_post_request()
		this.clean_input_box()
	}
}
