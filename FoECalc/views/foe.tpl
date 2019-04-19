% rebase('layout.tpl', title='Home Page', year=year)

<script>
var results = undefined;

 $().ready(function() {
	$.get("/goods", function(data) {
		var availableTags = data.goods;
		
		$("#amt").keyup (function() {
			var amount = parseFloat($("#amt").val());
			if (results != undefined && amount > 0) {			
				$.each(results.eras, function(i, v) {
					var val = Math.floor(v.Factor * amount) + " for " + amount + " " + results.val;
					$("#v" + i).html(val);
				});
			}
		})

		var ac = $("#tags").autocomplete({
			source: availableTags.sort(),
			select: function (event, ui) {
						$.ajax({
							type: "POST",
							url: "/rates", 
							contentType: "application/json",
							data: JSON.stringify({ selected: ui.item.value }), 
							success: function(data) {
								results = data;
								$("#era").html(data.name);
								apnd = "<table cellpadding='5'><thead><td><label>Age/Era</label></td><td><label>Factor</label></td><td><label>Goods</label></td><td><label>Trade Amount</label></td></thead>";
								$.each(data.eras, function(i,v) {
									apnd += "<tr><td>" + v.Name + "</td><td>" + v.Factor + "</td><td>";
									$.each(v.Goods, function(i2,v2) {
										if (i2 == v.Goods.length -1)
											apnd += v2;
										else
											apnd += v2 + ",&nbsp;";
									});
									apnd += "</td><td><span id='v" + i + "'></span></td></tr>";
								});
								apnd += "</table>";
								$("#pos").html(apnd);
							}
						});				
			}
		});				

		var wantAc = $("#wantTags").autocomplete({
			source: availableTags.sort(),
			select: function (event, ui) {
						$.ajax({
							type: "POST",
							url: "/rates", 
							contentType: "application/json",
							data: JSON.stringify({ selected: ui.item.value }), 
							success: function(data) {
								results = data;
								$("#wantEra").html(data.name);
								apnd = "<table cellpadding='5'><thead><td><label>Age/Era</label></td><td><label>Factor</label></td><td><label>Goods</label></td><td><label>Trade Amount</label></td></thead>";
								$.each(data.eras, function(i,v) {
									apnd += "<tr><td>" + v.Name + "</td><td>" + v.Factor + "</td><td>";
									$.each(v.Goods, function(i2,v2) {
										if (i2 == v.Goods.length -1)
											apnd += v2;
										else
											apnd += v2 + ",&nbsp;";
									});
									apnd += "</td><td><span id='v" + i + "'></span></td></tr>";
								});
								apnd += "</table>";
								$("#wantPos").html(apnd);
							}
						});				
			}
		});
	
	});

});
</script>

<div class="ui-widget">
<div style="font-weight:bold;">I Have</div>
  <label for="tags">Tags: </label>
  <input id="tags" />
  &nbsp;&nbsp;
  <label for="era">Era: </label>
  <span id="era"></span>
  &nbsp;&nbsp;
  <label for="amt">Amount: </label>
  <input id="amt" type="text" />
  <br /><br />
  <label>Trades with</label>
  <div id="pos" ></div>
  <BR><BR>

  <!-- 
<div style="font-weight:bold;">I Want It!</div>
  <label for="wantTags">Tags: </label>
  <input id="wantTags" />
  &nbsp;&nbsp;
  <label for="wantEra">Era: </label>
  <span id="wantEra"></span>
  &nbsp;&nbsp;
  <label for="wantAmt">Amount: </label>
  <input id="wantAmt" type="text" />
  <br /><br />
  <label>Trades with</label>
  <div id="wantPos"></div>
</div>
-->