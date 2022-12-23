const nombreInput = document.getElementById("nombre");
const apellidoInput = document.getElementById("apellido");
const agregar = document.getElementById("agregar-btn");
const BACK_URL = "http://localhost:5000";
const tabla = document.getElementById("tabla");

const tablaHeader = document.createElement("tr");
tablaHeader.innerHTML = `
  <th>id</th>
  <th>nombre</th>
  <th>apellido</th>`;

const agregarUsuario = async (data) => {
  const resultado = await fetch(`${BACK_URL}/usuarios`, {
    method: "POST",
    body: JSON.stringify(data),
    headers: { "Content-Type": "application/json" },
  });

  await resultado.json();
  await listarUsuarios();
};

const listarUsuarios = async () => {
  const resultado = await fetch(`${BACK_URL}/usuarios`, { method: "GET" });
  const data = await resultado.json();
  tabla.innerText = "";
  tabla.appendChild(tablaHeader);

  data.content.forEach((info, index) => {
    const fila = document.createElement("tr");
    const tdId = document.createElement("td");
    const tdNombre = document.createElement("td");
    const tdApellido = document.createElement("td");
    tdId.innerText = index;
    tdNombre.innerText = info.nombre;
    tdApellido.innerText = info.apellido;
    fila.appendChild(tdId);
    fila.appendChild(tdNombre);
    fila.appendChild(tdApellido);
    tabla.appendChild(fila);
  });
};

const agregarBtnClick = async (e) => {
  e.preventDefault();
  const nombre = nombreInput.value;
  const apellido = apellidoInput.value;

  await agregarUsuario({ nombre, apellido });
};

agregar.addEventListener("click", agregarBtnClick);
listarUsuarios();
