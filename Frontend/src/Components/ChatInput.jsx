import { useState } from "react";

export default function ChatInput({ sendMessage }) {

  const [message, setMessage] = useState("");

  function handleSend() {

    sendMessage(message);

    setMessage("");
  }

  return (

    <div className="flex p-4 gap-3 bg-white border-t">

      <input
        className="flex-1 border rounded-xl px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500"
        placeholder="Ask anything..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            handleSend();
          }
        }}
      />

      <button
        onClick={handleSend}
        className="bg-blue-600 hover:bg-blue-700 transition text-white px-6 rounded-xl"
      >
        Send
      </button>

    </div>

  );
}