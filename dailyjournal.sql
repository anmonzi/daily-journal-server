DROP TABLE Entry;
DROP TABLE Mood;


CREATE TABLE `Entry` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `mood_id` INTEGER,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);


CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);



INSERT INTO `Mood` VALUES (null, 'Great');
INSERT INTO `Mood` VALUES (null, 'Ok');
INSERT INTO `Mood` VALUES (null, 'Meh');
INSERT INTO `Mood` VALUES (null, 'Frustrated');
INSERT INTO `Mood` VALUES (null, 'Angery');

INSERT INTO `Entry` VALUES (null, 'HTML & CSS', 'We talked about HTML components and how to make grid layouts with Flexbox in CSS.', '04/07/2021', 1);
INSERT INTO `Entry` VALUES (null, 'Git & Github workflow', 'We learned how to work in teams and push code to Github, review, and merge code into the main branch.', '04/14/2021', 2);
INSERT INTO `Entry` VALUES (null, 'JavaScript', 'We started learning the basic JavaScript functions, objects, arrays, and how to console.log in our terminal.', '04/19/2021', 3);
INSERT INTO `Entry` VALUES (null, 'Javascript Debugging and Event Listeners', 'We learned how to debug in Chrome devtools and got introduced to event listeners.', '04/22/2021', 3);


SELECT * FROM Mood;
SELECT * FROM Entry;