import ToastMessage from '../../utils/toaster/toaster';
import Header from '../../components/Header/header';
import { getReportData } from '../../services/assessment';
import { useState, useEffect } from 'react';

export default function Report() {
    const [reportData, setReportData] = useState([]);

    useEffect(() => {
        async function fetchData() {
            try {
                const reportResponse = await getReportData();
                setReportData(reportResponse);
            } catch (error) {
                ToastMessage.error("Failed to fetch report data.");
                console.error(error);
            }
        }

        fetchData();
    }, []);

    return (
        <>
            <Header />

            <div className="container mx-auto px-4 py-8">
                <h1 className="text-3xl font-bold mb-6 text-center text-gray-800 py-4">📊 System Cleanup Reports</h1>

                {reportData && reportData.length > 0 ? (
                    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                        {reportData.map((data, index) => (
                            <div key={index} className="bg-white shadow-md rounded-lg p-4 border border-gray-200 hover:shadow-lg transition-shadow duration-300 mt-2">
                                <h3 className="text-xl font-semibold text-gray-700 mb-4">Report #{index + 1}</h3>
                                <ul className="text-gray-600 space-y-2">
                                    <li>
                                        <span className="font-medium">Users Deleted:</span> {data.users_deleted}
                                    </li>
                                    <li>
                                        <span className="font-medium">Active Users Remaining:</span> {data.active_users_remaining}
                                    </li>
                                    <li>
                                        <span className="font-medium">Timestamp:</span>{' '}
                                        {new Date(data.timestamp).toLocaleString()}
                                    </li>
                                </ul>
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="text-center py-12">
                        <p className="text-lg text-gray-500">🚫 No reports available yet.</p>
                    </div>
                )}
            </div>

        </>
    );
}
