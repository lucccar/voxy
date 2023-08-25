let form = document.getElementById("word-form")[0]["form"];
const home = "http://localhost:7070/";
let count = "http://localhost:7070/count";

async function updatePage(event) {
  console.log({ event });

  var checkedBoxes = document.querySelectorAll("input[type=checkbox]:checked");
  let delimiters = [];
  Array.from(checkedBoxes).map((box) => delimiters.push(box.value));

  const formData = {
    word: event.target[0].value,
    delimiters: delimiters,
  };

  const jsonData = JSON.stringify(formData);

  fetch(count, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: jsonData,
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("result").innerHTML = data;
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

form.addEventListener("submit", function (e) {
  e.preventDefault();
  updatePage(e);
});
