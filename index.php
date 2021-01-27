<form method='post' action='affichage_temperature.php'>
<fieldset>
<label for='ville'>Selectionnez une ville: </label>
<select name='ville' id='ville' required>
    <?php
    $dbh = new PDO('mysql:host=localhost;dbname=bdd_temperaturesvilles', 'root', '');
    $reponse = $dbh->query('SELECT * FROM temperaturevilles');
        while($donnees = $reponse->fetch())
        {
            ?>
            <option value="<?php echo $donnees['ville']; ?>"> 
            <?php echo ucwords($donnees['ville']); ?></option>
            <?php
        }?>

    </select>

<input type='submit' name='Valider'>
</fieldset>
</form>