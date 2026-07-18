import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    uploadPhoto(fileName),
    signUpUser(firstName, lastName),
  ]).then((results) => {
    return results.map((result) => {
      return {
        status: result.status,
        // If fulfilled, use result.value; if rejected, use result.reason
        value: result.status === 'fulfilled' ? result.value : result.reason,
      };
    });
  });
}
