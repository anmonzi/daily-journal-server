DROP TABLE Entries;
DROP TABLE Moods;


CREATE TABLE `Entries` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`concept`	TEXT NOT NULL,
	`entry`	TEXT NOT NULL,
    `date` TEXT NOT NULL,
    `mood_id` INTEGER,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);


CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);



INSERT INTO `Moods` VALUES (null, 'Great');
INSERT INTO `Moods` VALUES (null, 'Ok');
INSERT INTO `Moods` VALUES (null, 'Meh');
INSERT INTO `Moods` VALUES (null, 'Frustrated');
INSERT INTO `Moods` VALUES (null, 'Angery');

INSERT INTO `Entries` VALUES (null, 'HTML & CSS', 'We talked about HTML components and how to make grid layouts with Flexbox in CSS.', '04/07/2021', 1);
INSERT INTO `Entries` VALUES (null, 'Git & Github workflow', 'We learned how to work in teams and push code to Github, review, and merge code into the main branch.', '04/14/2021', 2);
INSERT INTO `Entries` VALUES (null, 'JavaScript', 'We started learning the basic JavaScript functions, objects, arrays, and how to console.log in our terminal.', '04/19/2021', 3);
INSERT INTO `Entries` VALUES (null, 'Javascript Debugging and Event Listeners', 'We learned how to debug in Chrome devtools and got introduced to event listeners.', '04/22/2021', 3);


SELECT * FROM Moods;
SELECT * FROM Entries;