import React from "react";
import MainCard from "./MainCard";
import {
  TextField,
  CircularProgress,
  Card,
  CardContent,
  Typography,
  Grid,
  Divider,
  CardActions,
  Button,
  //   item,
} from "@mui/material";
import Avatar from "@mui/material/Avatar";
import UserIcon from "./219970.png";
import BotIcon from "./bot.jpg";
import SyncLoader from "react-spinners/SyncLoader";
class Chatbot extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      ws: null,
      messages: [],
      inputValue: "",
      lastUserMessageIndex: -1, // Index of the last user message
      botTyping: true,
    };
  }

  componentDidMount() {
    console.log("M O U N T I N G");
    // Establish WebSocket connection
    if (!this.state.ws) {
      const clientUrl = "https://dental-chatbot-06mx.onrender.com/";
      const websocketUrl =
        clientUrl.replace("http", "ws").replace("https", "wss") +
        `ws/${new Date().getTime()}`;
      const ws = new WebSocket(websocketUrl);
      ws.onopen = () => {
        console.log("WebSocket connection established.");
      };
      ws.onmessage = (event) => {
        this.handleBotMessage(event.data);
      };
      ws.onclose = () => {
        console.log("WebSocket connection closed.");
      };
      this.setState({ ws });
    }
  }
  componentDidUpdate() {
    this.scrollToBottom();
  }
  scrollToBottom = () => {
    if (this.messagesEnd) {
      this.messagesEnd.scrollTop = this.messagesEnd.scrollHeight;
    }
  };
  componentWillUnmount() {
    // Clean up WebSocket connection
    const { ws } = this.state;
    if (ws) {
      ws.send("Closing connection");
      ws.close();
    }
  }

  handleBotMessage = (message) => {
    console.log(message);
    // Append new message to the last user message
    this.setState((prevState) => {
      const messages = [...prevState.messages];
      //   debugger;
      const lastUserMessageIndex = prevState.lastUserMessageIndex;
      if (lastUserMessageIndex !== -1) {
        const lastUserMessage = messages[lastUserMessageIndex];
        if (!lastUserMessage.partialBotMessage) {
          lastUserMessage.partialBotMessage = message;
        } else {
          lastUserMessage.partialBotMessage += message;
        }
      } else {
        // If there's no last user message, create a new one
        messages.push({ type: "user", text: "", partialBotMessage: message });
        return { messages, lastUserMessageIndex: messages.length - 1 };
      }
      return { messages };
    });
    this.setState({ botTyping: false });
  };

  sendMessage = () => {
    this.setState({ botTyping: true });
    // Send user message to WebSocket server
    const { ws, inputValue } = this.state;
    if (ws) {
      ws.send(inputValue);
      this.setState((prevState) => ({
        messages: [
          ...prevState.messages,
          { type: "user", text: inputValue, partialBotMessage: "" },
        ],
        inputValue: "",
        lastUserMessageIndex: prevState.messages.length, // Update last user message index
      }));
    }
  };

  render() {
    const { messages, inputValue, botTyping } = this.state;
    return (
      <div>
        <div>
          <MainCard
            className="card"
            style={{
              minHeight: "400px",
              maxHeight: "85vh",
              maxWidth: "90%",
              border: "none",
              backgroundColor: "rgb(255 252 252 / 42%)",
            }}
          >
            <CardContent style={{ padding: 0 }}>
              <div>
                <h1
                  style={{
                    display: "flex",
                    justifyContent: "flex-start",
                  }}
                >
                  Prompt
                </h1>

                <h4
                  style={{
                    display: "flex",
                    justifyContent: "flex-start",
                    fontWeight: "400",
                  }}
                >
                  We connect you with doctors who have a proven track record of
                  successfully trating similar conditions.
                </h4>
                <hr />
                <div
                  id="response"
                  style={{ overflowY: "auto", height: "63vh" }}
                  ref={(el) => {
                    this.messagesEnd = el;
                  }}
                >
                  {messages.map((message, index) => (
                    <div key={index}>
                      {message.text && (
                        <div
                          style={{
                            display: "flex",
                            justifyContent: "flex-end",
                            margin: "15px 20px 15px 15px",
                          }}
                        >
                          <div
                            style={{
                              backgroundColor: "#ffff",
                              padding: "8px",
                              borderRadius: "16px",
                              minWidth: "70px",
                              marginRight: "6px",
                              boxShadow: "0 2px 14px 0 rgb(32 40 45 / 8%)",
                            }}
                          >
                            {message.text}
                          </div>
                          <div style={{ marginRight: "8px" }}>
                            <Avatar alt="User" src={UserIcon} />
                          </div>
                        </div>
                      )}
                      {message.partialBotMessage && (
                        <div
                          style={{
                            display: "flex",
                            justifyContent: "flex-start",
                            margin: "0 50px 10px 15px",
                          }}
                        >
                          <div style={{ marginLeft: "8px" }}>
                            <Avatar alt="Bot" src={BotIcon} />
                          </div>
                          <div
                            style={{
                              backgroundColor: "rgb(118 213 203)",
                              padding: "8px",
                              borderRadius: "16px",
                              minWidth: "70px",
                              marginLeft: "6px",
                              boxShadow: "0 2px 14px 0 rgb(32 40 45 / 8%)",
                            }}
                          >
                            {message.partialBotMessage}
                          </div>
                        </div>
                      )}
                    </div>
                  ))}
                  {botTyping && (
                    <div
                      style={{
                        display: "flex",
                        alignItems: "center",
                        margin: "0 50px 10px 15px",
                      }}
                    >
                      <Avatar alt="Bot" src={BotIcon} />
                      <SyncLoader
                        color={"#42837c"}
                        loading={true}
                        // cssOverride={override}
                        size={10}
                        aria-label="Loading Spinner"
                        data-testid="loader"
                      />
                    </div>
                  )}
                </div>
                <div
                  id="input-container"
                  style={{ display: "flex", alignItems: "center" }}
                >
                  <input
                    type="text"
                    value={inputValue}
                    onChange={(e) =>
                      this.setState({ inputValue: e.target.value })
                    }
                    className="placeholder-red"
                    placeholder="Enter a prompt here..."
                    style={{
                      flex: "1",
                      borderRadius: "20px",
                      padding: "10px",
                      marginRight: "10px",
                      border: "1px solid #ccc",
                      background: "#5e6262e3",
                    }}
                    onKeyPress={(e) => {
                      if (e.key === "Enter") {
                        this.sendMessage();
                      }
                    }}
                  />
                  <button
                    onClick={this.sendMessage}
                    style={{
                      marginLeft: "-48px",
                      width: "38px",
                      height: "37px",
                      borderRadius: "50%",
                      border: "none",
                      backgroundColor: "rgb(255, 97, 0)",
                      color: "#fff",
                      cursor: "pointer",
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      strokeWidth="2"
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      className="feather feather-send"
                    >
                      <line x1="22" y1="2" x2="11" y2="13" />
                      <polygon points="22 2 15 22 11 13 2 9 22 2" />
                    </svg>
                  </button>
                </div>
              </div>
            </CardContent>
          </MainCard>
        </div>
      </div>
    );
  }
}

export default Chatbot;
