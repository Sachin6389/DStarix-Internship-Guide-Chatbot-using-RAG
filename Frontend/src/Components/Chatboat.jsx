
import { useState, useEffect, useRef } from "react";
import axios from "axios";
import Message from "./Message"
import ChatInput from "./ChatInput"

function Chatboat() {
 const API = import.meta.env.VITE_BACKEND_URL;
  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "👋 Hello! I'm your DStarix Internship Guide Chatbot. How can I help you today?",
    },
  ]);

  const [loading, setLoading] = useState(false);

  const bottomRef = useRef();

  useEffect(() => {
    bottomRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  async function sendMessage(text) {
    if (!text.trim()) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text,
      },
    ]);

    setLoading(true);

    try {
      const res = await axios.post( `${API}/chat`, {
        question: text,
      });
      console.log(res)

      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: res.data.response,
        },
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          sender: "bot",
          text: "❌ Unable to connect to server.",
        },
      ]);
    }

    setLoading(false);
  }

  return (
    <div className="bg-white shadow-2xl rounded-2xl w-full max-w-3xl overflow-hidden">

      <div className="bg-blue-600 text-white text-center py-5 text-2xl font-bold">
        DStarix Internship Guide Chatbot
      </div>

      <div className="h-[500px] overflow-y-auto p-6 bg-gray-50">

        {messages.map((msg, index) => (
          <Message key={index} message={msg} />
        ))}

        {loading && (
          <Message
            message={{
              sender: "bot",
              text: "Typing...",
            }}
          />
        )}

        <div ref={bottomRef}></div>

      </div>

      <ChatInput sendMessage={sendMessage} />

    </div>
  );
}
export default Chatboat;