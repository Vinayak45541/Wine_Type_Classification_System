import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL || "http://127.0.0.1:8000",
});

export const predictWine = async (data) => {
  const res = await API.post("/predict", data);
  return res.data;
};