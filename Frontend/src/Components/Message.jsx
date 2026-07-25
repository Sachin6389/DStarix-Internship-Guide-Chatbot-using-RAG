import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

export default function Message({ message }) {
  const isUser = message.sender === "user";

  return (
    <div className={`flex mb-4 ${isUser ? "justify-end" : "justify-start"}`}>
      {isUser ? (
        <div className="max-w-[80%] rounded-2xl rounded-br-sm bg-blue-600 text-white px-4 py-3 shadow">
          {message.text}
        </div>
      ) : (
        <div className="max-w-[80%] rounded-2xl rounded-bl-sm border bg-white px-4 py-3 shadow">
          <article className="prose prose-sm max-w-none">
            <ReactMarkdown remarkPlugins={[remarkGfm]}
            
      >
              {message.text}
            </ReactMarkdown>
          </article>
        </div>
      )}
    </div>
  );
}