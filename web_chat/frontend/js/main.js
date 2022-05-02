const message = new Message("#message-input", "http://localhost:8000/web-chat/");
const renderer = new Renderer();

renderer.render_all_posts().then()
set_keyboard_shortcuts();

function main() {
	message.send_message();
}
