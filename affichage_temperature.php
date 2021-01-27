<?php
$dbh = new PDO('mysql:host=localhost;dbname=bdd_temperaturesvilles', 'root', '');
$dbh->query("SET lc_time_names = 'fr_FR'");
$ma_ville = htmlspecialchars($_POST['ville']);
//$res = $dbh->query("SELECT temperatures, ville FROM `temperaturevilles` WHERE ville in ('la buisse', 'plouhinec', 'vic-fezensac', 'rouen')");
$res = $dbh->prepare("SELECT temperatures, DATE_FORMAT(last_update,'Le %d %M %Y à %H h %i') as last_update FROM temperaturevilles WHERE ville = ?");
$res->execute(array($ma_ville));

while ($donnees=$res->fetch())
{
    echo $donnees['last_update']." à ".ucwords($ma_ville)." il faisait ".$donnees['temperatures']. " degrés.";
    echo"<br><br>";
}

echo "<br>";
echo "<a href='index.php'>retour</a>";

?>