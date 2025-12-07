import { useState } from "react";
import api, { setAuthToken } from "../api";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  async function login() {
    try {
      const form = new FormData();
      form.append("username", email);
      form.append("password", password);

      const res = await api.post("/auth/login", form);
      const token = res.data.access_token as string;

      localStorage.setItem("token", token);
      setAuthToken(token);

      navigate("/predict");
    } catch {
      setError("Invalid login credentials");
    }
  }

  return (
    <div className="app-root">
      <div className="card">
        <h1 className="card-title">TicketBrain</h1>
        <p className="card-subtitle">
          Sign in to access the ticket priority model dashboard.
        </p>

        <div className="form-group">
          <label className="label">Email</label>
          <input
            className="input"
            placeholder="you@example.com"
            value={email}
            onChange={e => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label className="label">Password</label>
          <input
            className="input"
            type="password"
            placeholder="••••••••"
            value={password}
            onChange={e => setPassword(e.target.value)}
          />
        </div>

        <button className="btn btn-primary" onClick={login}>
          Login
        </button>
         <p>
  Don't have an account? <a href="/register">Register here</a>
</p>
<p style={{opacity:0.6}}>
  Forgot password? Contact admin.
</p>



        {error && (
          <p style={{ color: "#fecaca", marginTop: 10, fontSize: "0.85rem" }}>
            {error}
          </p>
        )}

      </div>
    </div>
  );
}
