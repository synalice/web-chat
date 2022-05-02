const message = new Message("#message-input", "https://syn-server.tech/web-chat/");
const renderer = new Renderer();

renderer.render_all_posts().then()
set_keyboard_shortcuts();

async function main() {
	await message.send_message();
	await renderer.remove_all_posts();
	await renderer.render_all_posts();
}
