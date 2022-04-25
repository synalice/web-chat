class Message {

	constructor(input_box_name) {
		this.input_box_name = input_box_name
	}

	text;

	get_message_text() {
		return this.text = document.querySelector(`${this.input_box_name}`).value;
	}

	clean_input_box() {
		return document.querySelector(`${this.input_box_name}`).value = "";
	}
}


class Sender {

	constructor(api_url) {
		this.api_url = api_url
	}

	static message;
	static payload;

	static prepare_message(message_text) {
		Sender.message = {
			"id": 1, "date": get_current_date(), "content": message_text
		}
	}

	static prepare_payload() {
		Sender.payload = {
			method: "POST", body: JSON.stringify(Sender.message), headers: {
				"Access-Control-Allow-Origin": "*", "Content-Type": "application/json",
			},
		};
	}

	send_post_request(message_text) {
		Sender.prepare_message(message_text)
		Sender.prepare_payload();

		fetch(this.api_url, Sender.payload).then(() => {
		});
	}

}
