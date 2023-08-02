<!DOCTYPE html>
<html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
<style>
.toggle-container {
  position: relative;
  display: inline-block;
  width: 60px;
  height: 34px;
}

.toggle-switch {
  position: absolute;
  cursor: pointer;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: gray;
  transition: .4s;
  border-radius: 34px;
}

.toggle-switch::before {
  position: absolute;
  content: "";
  height: 26px;
  width: 26px;
  left: 4px;
  bottom: 4px;
  background-color: white;
  transition: .4s;
  border-radius: 50%;
}

.toggle-container.on .toggle-switch {
  background-color: #2196F3;
}

.toggle-container.on .toggle-switch::before {
  transform: translateX(26px);
}


</style>
</head>
<body>

<div class="toggle-container">
  <div class="toggle-switch"></div>
</div>

<script>
$(document).ready(function() {
  $(".toggle-container").click(function() {
    $(this).toggleClass("on");
  });
});

</script>


</body>
</html>
