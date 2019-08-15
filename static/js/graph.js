var data = {{ response.data| safe}}

var ctxL = document.getElementById("line-plot").getContext('2d');
var myLineChart = new Chart(ctxL, {
  type: 'line',
  data: {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
      {
        label: "My First dataset",
        data: [0, 30, 20, 30, 20, 30, 10],
        borderColor: ['#0099ff'],
        backgroundColor: ['transparent'],
        borderWidth: 2,
        pointBorderColor: "#fff",
      }
    ]
  },
  options: {
    responsive: true
  }
});