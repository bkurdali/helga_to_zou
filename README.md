# helga_to_zou
Python scripts for migrating a Helga database and files to Kitsu/Zou

* **Helga :** is an animation project management tool, tracking assets and tasks, and integrating with Tractor renderfarm to render and track rendered frames.
It's written in PHP by students, professors and staff at Hampshire College, and currently unmaintained (especially the 1.x branch)

* **Kitsu :** (made by [CG WIRE](https://cg-wire.com)) is a similar production tracker for animation. [Zou](https://zou.cg-wire.com/) which is its backend and paired with web-based APIs, and a client-side Python APIs that's [Gazu](https://gazu.cg-wire.com/)

Since Helga is unmaintained and depending on a fairly old version of PHP, these scripts are intended to be run once and migrate as much as possible of the project data and history to Zou, using direct database access to Helga's mysql database, and the Zou's REST APIs.

