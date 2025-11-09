import React from 'react';
import { Pie } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(ArcElement, Tooltip, Legend);

const PieChart = ({ data }) => {
  const chartData = {
    labels: ['Safe', 'Suspicious', 'Malicious'],
    datasets: [
      {
        data: data?.distribution || [70, 20, 10],
        backgroundColor: [
          'rgba(75, 192, 192, 0.6)',
          'rgba(255, 205, 86, 0.6)',
          'rgba(255, 99, 132, 0.6)',
        ],
        borderColor: [
          'rgba(75, 192, 192, 1)',
          'rgba(255, 205, 86, 1)',
          'rgba(255, 99, 132, 1)',
        ],
        borderWidth: 2,
      },
    ],
  };

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Threat Distribution',
      },
    },
  };

  return <Pie data={chartData} options={options} />;
};

export default PieChart;