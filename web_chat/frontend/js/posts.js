// TODO: refactor these functions to make them more reusable

function main() {
	let message_text = get_message_text();
	clean_input_box();
	post_message(message_text)
}

function clean_input_box() {
	return document.querySelector("#message-input").value = "";
}

function get_message_text() {
	return document.querySelector("#message-input").value;
}

function post_message(message_text) {
	let payload = {
		"id": 1, "date": "04/25/2022", "content": message_text
	};
	const options = {
		method: "POST", body: JSON.stringify(payload), headers: {
			"Access-Control-Allow-Origin": "*", "Content-Type": "application/json",
		},
	};
	fetch("http://127.0.0.1:8000/web-chat/posts/new", options);
}
