// This submits contents of #message-send input box when user presses ctrl+Enter
document.addEventListener('keydown', (event) => {
	if (event.ctrlKey && (event.key === "Enter")) {
		document.querySelector("#message-send").click();
	}
})

