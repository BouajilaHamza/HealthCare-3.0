let form = document.getElementById("form-id");

form.addEventListener("submit", async (event) => {

  event.preventDefault();

  const formData = new FormData(form);

  const data = Object.fromEntries(formData.entries());
  console.log(data);

  const json = JSON.stringify(data);
  console.log(json);

  const response = await fetch("/update_patient", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: json,
  });
  // Handle the response
  if (response.ok) {
    // Do something with the response data
    const result = await response.json();
    console.log(result);
  } else {
    // Handle the error
    console.error(response.status, response.statusText);
  }
});
