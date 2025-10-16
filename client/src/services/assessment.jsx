import api from "../api/api";

export async function getReportData() {
    const res = await api.get("/api/reports/latest/");
    return res.data;
}

export async function manualTrigger() {
    const res = await api.post('api/cleanup/trigger/', {})
    return res.data;
}