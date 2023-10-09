<html>

<head>
    <meta charset="utf-8">
    <title>Página do Futebol</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<?php
$ch = curl_init();
$urlApi = 'https://jsuol.com.br/c/monaco/utils/gestor/commons.js?file=commons.uol.com.br/sistemas/esporte/modalidades/futebol/campeonatos/dados/2023/30/dados.json';

curl_setopt($ch, CURLOPT_URL, $urlApi);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);

$resultApi = curl_exec($ch);

$arrayJsonApi = json_decode($resultApi, true);

// EQUIPES - START
$arrayEquipes = $arrayJsonApi['equipes'];
// FASES - START

// EQUIPES - END
$fase = $arrayJsonApi['ordem-fases'][0];
// FASES - END

// CLASSIFICAÇÃO - START
$arrayClassificacao = $arrayJsonApi['fases'][$fase]['classificacao']['grupo']['Único'];
// CLASSIFICAÇÃO - END

$arrayPontos = $arrayJsonApi['fases'][$fase]['classificacao']['equipe'];
?>

<body>
    <header class="cabecalho">
        <label class="label-cabecalho">Brasileirão Série A</label>
    </header>
    <table border="0px">
        <tr>
            <td></td>
            <td>Clube</td>
            <td></td>
            <td></td>
            <td>Pontos</td>
            <td>Jogos</td>
            <td>Vitórias</td>
            <td>Empates</td>
            <td>Derrotas</td>
            <td>GP</td>
            <td>GC</td>
            <td>SG</td>
        </tr>
<?php
$posicao = 1;

foreach ($arrayClassificacao as $keyClassificacao => $valueClassificacao) {
    $classeDestaque = '';
    if ($posicao <= 4) {
        $classeDestaque = 'libertadores libertadores4';
    } elseif ($posicao == 5 || $posicao == 6) {
        $classeDestaque = 'laranja';
    } elseif ($posicao >= 7 && $posicao <= 12) {
        $classeDestaque = 'verde';
    } elseif ($posicao >= 13 && $posicao <= 16) {

    } elseif ($posicao >= 17 && $posicao <= 20) {
        $classeDestaque = 'vermelho';
    }
?>
    <tr onclick="window.location.href='<?= $arrayEquipes[$valueClassificacao]['uri'] ?>'">
        <td class="<?= $classeDestaque ?>"></td>
        <td class="celula-interativa"><?= $posicao ?></td>
        <td class="celula-interativa"><img src="<?= $arrayEquipes[$valueClassificacao]['brasao'] ?>"></td>
        <td class="celula-interativa"><?= $arrayEquipes[$valueClassificacao]['nome-comum'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['pg']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['j']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['v']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['e']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['d']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['gp']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['gc']['total'] ?></td>
        <td class="celula-interativa"><?= $arrayPontos[$valueClassificacao]['sg']['total'] ?></td>
    </tr>
<?php
    $posicao++;
}
?>
    </table>
</body>
</html>