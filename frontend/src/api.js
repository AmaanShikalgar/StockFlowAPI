import axios from "axios";

const api = axios.create({
  baseURL: "https://stockflowapi-yvbr.onrender.com",
});

export default api;