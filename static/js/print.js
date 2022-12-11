// $('#downloadPDF').click(function () {
//     domtoimage.toPng(document.querySelector('.calCont'))
//         .then(function (blob) {
//             var pdf = new jsPDF('l', 'pt', [$('.calCont').width(), $('.calCont').height()]);
//             pdf.addImage(blob, 'PNG', 0, 0, $('.calCont').width(), $('.calCont').height());
//             pdf.save("print.pdf");

//             that.options.api.optionsChanged();
//         });
// });