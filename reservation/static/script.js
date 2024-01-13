document.addEventListener('DOMContentLoaded', function() {
    // Récupère la liste déroulante 'schedule'
    const scheduleSelect = document.getElementById('schedule');

    // Charge les horaires depuis le serveur Django avec AJAX
    fetch('/get_schedules/')
      .then(response => response.json())
      .then(data => {
        // Ajoute chaque horaire comme une option à la liste déroulante
        data.forEach(schedule => {
          const option = document.createElement('option');
          option.value = schedule.id;
          option.text = `${schedule.depart} - ${schedule.destination} - ${ new Date (schedule.schedule).toLocalesString() }`;
          scheduleSelect.add(option);
        });
      })
      .catch(error => console.error('Error fetching schedules:', error));
});
