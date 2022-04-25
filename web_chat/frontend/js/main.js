// Here is everything required for sending messages

function main() {
	message.get_message_text()
	message.clean_input_box()
	sender.send_post_request(message.text);
}
