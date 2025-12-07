import { useState } from "react";
import api from "../api";

export default function Register() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    try {
      await api.post("/auth/register", { email, password });
      setMessage("✅ Registration successful! You can now login.");
    } catch (err: any) {
      setMessage(
        err?.response?.data?.detail ||
          "❌ Registration failed. Try a different email."
      );
    }
  };

  return (
    <div style={{ padding: "40px", maxWidth: "400px", margin: "0 auto" }}>
      <h2>Register</h2>
      <input
        placeholder="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        style={{ width: "100%", marginBottom: "10px" }}
      />

      <button onClick={handleRegister} style={{ width: "100%" }}>
        Register
      </button>

      <p>{message}</p>
    </div>
  );
}
