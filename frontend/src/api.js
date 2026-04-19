import axios from "axios";

const api = axios.create({
  baseURL: "https://stockflowapi-1-e2hb.onrender.com",
});

export default api;