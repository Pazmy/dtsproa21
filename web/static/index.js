function init() {
  let x = document.getElementById("remove-b");
  if (x) {
    setTimeout(() => {
      x.remove();
    }, 4000);
  }

  const formatter = new Intl.NumberFormat("id-ID", {
    style: "currency",
    currency: "IDR",
    minimumFractionDigits: 2,
  });

  let nominal = document.querySelectorAll("#nominal");
  const name = document.querySelector("#nominal").textContent;
  nominal.forEach((elem) => {
    elem.innerHTML = formatter.format(elem.textContent);
    if (elem.textContent == "RpNaN") {
      elem.innerHTML = name;
      console.log(elem.innerHTML);
    }
  });
}
