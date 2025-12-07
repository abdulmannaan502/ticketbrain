import { Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Predict from "./pages/Predict";
import Protected from "./components/Protected";
import Register from "./pages/Register";



export default function App() {
  return (
    <Routes>
      <Route path="/register" element={<Register />} />
      <Route path="/" element={<Navigate to="/login" />} />
      <Route path="/login" element={<Login />} />
      <Route
        path="/predict"
        element={
          <Protected>
            <Predict />
          </Protected>
        }
      />
    </Routes>
  );
}
