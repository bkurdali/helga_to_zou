# helga_to_zou
Python scripts for migrating a Helga Database and files to Zou/Kitsu
* **Helga** is an Animation project management tool, tracking assets and tasks, and integrating with tractor renderfarm to render and track rendered frames.
It's written in PHP by students, professors and staff at Hampshire college, and currently unmaintained (especially the 1.x branch)
* **Kitsu/Zou**: Kitsu is a similar asset managment system for animation, pared with a web api, and a client side python api (gazu), made by https://cg-wire.comy 

Since Helga is unmaintained and depending on a fairly old version of PHP, these scripts are intended to be run once and migrate as much as possible of the project data and history to Zou, using direct database access to Helga's mysql database, and the zou api.

