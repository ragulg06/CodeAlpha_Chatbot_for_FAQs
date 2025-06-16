const toggle = document.getElementById("chatbot-toggle");
const frame = document.getElementById("chatbot-frame");

toggle.addEventListener("click", () => {
  frame.style.display = frame.style.display === "none" ? "block" : "none";
});
