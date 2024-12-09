const kue = require('kue');

const pushNotificationCode = kue.createQueue();
const jobData = {
  phoneNumber: '07044808811',
  message: 'Hi there!',
};

const job = pushNotificationCode.create('push_notification_code', jobData).save();

job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
