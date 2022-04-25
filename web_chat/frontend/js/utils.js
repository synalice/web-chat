function set_keyboard_shortcuts() {
	// This submits contents of #message-send input box when user presses ctrl+Enter
	document.addEventListener('keydown', (event) => {
		if (event.ctrlKey && (event.key === "Enter")) {
			document.querySelector("#message-send").click();
		}
	})
}

function get_current_date() {
	let current_date = new Date().toLocaleDateString();
	let current_time = new Date().toLocaleTimeString('en-US', {
		hour12: false, hour: "numeric", minute: "numeric", second: "numeric"
	});
	return current_date + " " + current_time;
}
