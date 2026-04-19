import { useState } from "react";
import api from "../api";

function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();

    try {
      await api.post("/register", {
        email,
        password,
      });

      alert("Registered successfully");
    } catch (err) {
      console.log(err.response?.data || err.message);
      alert("Error registering");
    }
  };

  return (
    <form onSubmit={handleRegister} className="auth-form">
      <h2 className="auth-heading">Create Account</h2>

      <input
        type="email"
        placeholder="Enter your email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <input
        type="password"
        placeholder="Enter your password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />

      <button className="btn" type="submit">
        Register
      </button>
    </form>
  );
}

export default Register;