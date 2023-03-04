import nodemailer from "nodemailer";

export const enviarCorreo = async (destinatario, texto) => {
  //                  SERVIDOR      | PUERTO
  // outlook > outlook.office365.com | 587
  // hotmail > smtp.live.com         | 587
  // gmail >   smtp.gmail.com        | 587
  // icloud >  smtp.mail.me.com      | 587
  // yahoo >   smtp.mail.yahoo.com   | 587
  const trasportador = nodemailer.createTransport({
    host: "smtp.gmail.com",
    port: 465,
    secure: true,
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASSWORD,
    },
  });

  const resultado = await trasportador.sendMail({
    subject: "Bienvenido a la aplicacion de calendarios",
    text: texto,
    to: destinatario,
    from: process.env.EMAIL_USER,
  });

  console.log(resultado);
};
