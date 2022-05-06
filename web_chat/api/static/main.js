function setKeyboardShortcuts() {
	// This submits contents of #message-send input box when user presses ctrl+Enter
	document.addEventListener('keydown', (event) => {
		if (event.ctrlKey && (event.key === "Enter")) {
			document.querySelector("#message-send").click();
		}
	})
}

async function sendMessage(inputBox) {
	const message = document.querySelector(inputBox).value;
	const payload = {
		method: "PUT", body: JSON.stringify({"content": message}), headers: {
			"Access-Control-Allow-Origin": "*", "Content-Type": "application/json",
		}
	}
	await fetch("http://localhost:8000/web-chat/posts/new", payload)
}

async function clearInputBox(inputBox) {
	document.querySelector(inputBox).value = "";
}

setKeyboardShortcuts()

async function main() {
	await sendMessage("#message-input");
	await clearInputBox("#message-input");
	window.location.reload(true);
}
