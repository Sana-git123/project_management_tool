const ctx = document.getElementById("myChart");

new Chart(ctx, {
    type: "doughnut",
    data: {
        labels: [
            "Completed projects",
            "Overdue projects",
            "Project in progress",
        ],
        datasets: [
            {
                label: "Count",
                data: [200, 150, 250],
                backgroundColor: ["#7FCC87", "#E27171", "#90A5EF"],
                hoverOffset: 4,
                borderRadius:8,
                borderWidth: 5,
            },
        ],
    },
});
