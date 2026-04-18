import { useState } from "react";
import api from "./api";

function Login({onLogin}) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
  e.preventDefault();

  try {
    const formData = new URLSearchParams();
    formData.append("username", email);   // IMPORTANT
    formData.append("password", password);

    const res = await api.post("/login", formData, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
        },
      });

    localStorage.setItem("token", res.data.access_token);
    onLogin(res.data.access_token);
  } catch (err) {
    console.log(err);
    alert("Login failed");
  }
};

  return (
    <div>
      <h2>Login</h2>

      <form onSubmit={handleLogin}>
        <input placeholder="Email" onChange={(e) => setEmail(e.target.value)} />
        <br />

        <input
          placeholder="Password"
          type="password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <br />

        <button>Login</button>
      </form>
    </div>
  );
}

export default Login;