import axios from "axios";

const api = axios.create({
  baseURL: "https://abdulmannaan1-ticketbrain-backend.hf.space",
});

// Load token on refresh / init
const token = localStorage.getItem("token");
if (token) {
  api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
}

export const setAuthToken = (token: string | null) => {
  if (token) {
    api.defaults.headers.common["Authorization"] = `Bearer ${token}`;
  } else {
    delete api.defaults.headers.common["Authorization"];
  }
};

export default api;
