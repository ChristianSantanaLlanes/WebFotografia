<div class="instagram">
    		<div class="instagram_content">
    			<ul>
    				<li class="follow">
    					<div class="following">
    						<img class="svg" src="./img/svg/Facebook-Logo.wine.svg" alt="" />
    						<h3><a href="#">@FotoFly</a></h3>
    						<p>Siganme en Facebook</p>
    					</div>
    				</li>
    				<li>
    					<img src="img/facebook/boda.jpg" alt="" />
    				</li>
    				<li>
    					<img src="img/facebook/bebe.jpg" alt="" />
    				</li>
    				<li>
    					<img src="img/facebook/estudiante.jpg" alt="" />
    				</li>
    				<li>
    					<img src="img/facebook/graduacion.jpg" alt="" />
    				</li>
    				<li>
    					<img src="img/facebook/nino.jpg" alt="" />
    				</li>
    				<li>
    					<img src="img/facebook/nino2.jpg" alt="" />
    				</li>
    			</ul>
    		</div>
    	</div>
    	<div class="copyright">
    		<?php 
// No argument required for current year.
// Otherwise, pass start year as a 4-digit value.
function auto_copyright($startYear = null) {
	$thisYear = date('Y');  // get this year as 4-digit value
    if (!is_numeric($startYear)) {
		$year = $thisYear; // use this year as default
	} else {
		$year = intval($startYear);
	}
	if ($year == $thisYear || $year > $thisYear) { // $year cannot be greater than this year - if it is then echo only current year
		echo "&copy; $thisYear"; // display single year
	} else {
		echo "&copy; $year&ndash;$thisYear"; // display range of years
	}   
 } 
 ?>

<?php auto_copyright(2022);  // 2010 - Current ?>
    		<span>. Diseñado por <a href="#">ChrisVis</a></span>
    	</div>