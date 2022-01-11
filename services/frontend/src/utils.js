
export function generatePassword() {
    var length = 8,
        charset = "abcdefghijklmnoprstuwxyzABCDEFGHIJKLMNOPRSTUWXYZ0123456789!@#$%^&*",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
  return retVal;
}

export function padDate(value, paddingSize = 2, paddingValue = '0') {
    return `${value}`.padStart(paddingSize, paddingValue);
}

export function formatDate (datestr) {
    let date = new Date(Date.parse(datestr));
    const dateStr = `${date.getFullYear()}-${padDate(date.getMonth()+1)}-${padDate(date.getDate())}`;
    const timeStr = `${padDate(date.getHours())}:${padDate(date.getMinutes())}`;
    return `${dateStr} ${timeStr}`;
}

export function saveRecording(response, filename='analiza.wav') {
    const blob = new Blob([response.data], { type: 'application/octet-stream' });
    const fileLink = document.createElement('a');

    fileLink.href = window.URL.createObjectURL(blob);
    fileLink.target = '_blank';
    fileLink.setAttribute('download', filename);
    document.body.appendChild(fileLink);
    fileLink.click();
    document.body.removeChild(fileLink);
}