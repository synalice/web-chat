const message = new Message("#message-input", "http://127.0.0.1:8000/web-chat/posts/new");
set_keyboard_shortcuts();

function main() {
	message.send_message();
}
