import api from "../api/api";

export async function getReportData() {
    const res = await api.get("/api/cleanup-reports/");
    return res.data;
}

export async function manualTrigger() {
    const res = await api.post('api/trigger/', {})
    return res.data;
}