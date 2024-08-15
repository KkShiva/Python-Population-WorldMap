# import pygal library 
import pygal 
import pypopulation
# create a world map 
worldmap = pygal.maps.world.World() 

# set the title of the map 
worldmap.title = 'Countries Population Data'

# adding the countries 
worldmap.add('Population', { 
'ad' : pypopulation.get_population('ad'),
'ae' : pypopulation.get_population('ae'),
'af' : pypopulation.get_population('af'),
'al' : pypopulation.get_population('al'),
'am' : pypopulation.get_population('am'),
'ao' : pypopulation.get_population('ao'),
'aq' : pypopulation.get_population('aq'),
'ar' : pypopulation.get_population('ar'),
'at' : pypopulation.get_population('at'),
'au' : pypopulation.get_population('au'),
'az' : pypopulation.get_population('az'),
'ba' : pypopulation.get_population('ba'),
'bd' : pypopulation.get_population('bd'),
'be' : pypopulation.get_population('be'),
'bf' : pypopulation.get_population('bf'),
'bg' : pypopulation.get_population('bg'),
'bh' : pypopulation.get_population('bh'),
'bi' : pypopulation.get_population('bi'),
'bj' : pypopulation.get_population('bj'),
'bn' : pypopulation.get_population('bn'),
'bo' : pypopulation.get_population('bo'),
'br' : pypopulation.get_population('br'),
'bt' : pypopulation.get_population('bt'),
'bw' : pypopulation.get_population('bw'),
'by' : pypopulation.get_population('by'),
'bz' : pypopulation.get_population('bz'),
'ca' : pypopulation.get_population('ca'),
'cd' : pypopulation.get_population('cd'),
'cf' : pypopulation.get_population('cf'),
'cg' : pypopulation.get_population('cg'),
'ch' : pypopulation.get_population('ch'),
'ci' : pypopulation.get_population('ci'),
'cl' : pypopulation.get_population('cl'),
'cm' : pypopulation.get_population('cm'),
'cn' : pypopulation.get_population('cn'),
'co' : pypopulation.get_population('co'),
'cr' : pypopulation.get_population('cr'),
'cu' : pypopulation.get_population('cu'),
'cv' : pypopulation.get_population('cv'),
'cy' : pypopulation.get_population('cy'),
'cz' : pypopulation.get_population('cz'),
'de' : pypopulation.get_population('de'),
'dj' : pypopulation.get_population('dj'),
'dk' : pypopulation.get_population('dk'),
'do' : pypopulation.get_population('do'),
'dz' : pypopulation.get_population('dz'),
'ec' : pypopulation.get_population('ec'),
'ee' : pypopulation.get_population('ee'),
'eg' : pypopulation.get_population('eg'),
'eh' : pypopulation.get_population('eh'),
'er' : pypopulation.get_population('er'),
'es' : pypopulation.get_population('es'),
'et' : pypopulation.get_population('et'),
'fi' : pypopulation.get_population('fi'),
'fr' : pypopulation.get_population('fr'),
'ga' : pypopulation.get_population('ga'),
'gb' : pypopulation.get_population('gb'),
'ge' : pypopulation.get_population('ge'),
'gf' : pypopulation.get_population('gf'),
'gh' : pypopulation.get_population('gh'),
'gl' : pypopulation.get_population('gl'),
'gm' : pypopulation.get_population('gm'),
'gn' : pypopulation.get_population('gn'),
'gq' : pypopulation.get_population('gq'),
'gr' : pypopulation.get_population('gr'),
'gt' : pypopulation.get_population('gt'),
'gu' : pypopulation.get_population('gu'),
'gw' : pypopulation.get_population('gw'),
'gy' : pypopulation.get_population('gy'),
'hk' : pypopulation.get_population('hk'),
'hn' : pypopulation.get_population('hn'),
'hr' : pypopulation.get_population('hr'),
'ht' : pypopulation.get_population('ht'),
'hu' : pypopulation.get_population('hu'),
'id' : pypopulation.get_population('id'),
'ie' : pypopulation.get_population('ie'),
'il' : pypopulation.get_population('il'),
'in' : pypopulation.get_population('in'),
'iq' : pypopulation.get_population('iq'),
'ir' : pypopulation.get_population('ir'),
'is' : pypopulation.get_population('is'),
'it' : pypopulation.get_population('it'),
'jm' : pypopulation.get_population('jm'),
'jo' : pypopulation.get_population('jo'),
'jp' : pypopulation.get_population('jp'),
'ke' : pypopulation.get_population('ke'),
'kg' : pypopulation.get_population('kg'),
'kh' : pypopulation.get_population('kh'),
'kp' : pypopulation.get_population('kp'),
'kw' : pypopulation.get_population('kw'),
'kz' : pypopulation.get_population('kz'),
'la' : pypopulation.get_population('la'),
'lb' : pypopulation.get_population('lb'),
'li' : pypopulation.get_population('li'),
'lk' : pypopulation.get_population('lk'),
'lr' : pypopulation.get_population('lr'),
'ls' : pypopulation.get_population('ls'),
'lt' : pypopulation.get_population('lt'),
'lu' : pypopulation.get_population('lu'),
'lv' : pypopulation.get_population('lv'),
'ly' : pypopulation.get_population('ly'),
'ma' : pypopulation.get_population('ma'),
'mc' : pypopulation.get_population('mc'),
'md' : pypopulation.get_population('md'),
'me' : pypopulation.get_population('me'),
'mg' : pypopulation.get_population('mg'),
'mk' : pypopulation.get_population('mk'),
'ml' : pypopulation.get_population('ml'),
'mm' : pypopulation.get_population('mm'),
'mn' : pypopulation.get_population('mn'),
'mo' : pypopulation.get_population('mo'),
'mr' : pypopulation.get_population('mr'),
'mt' : pypopulation.get_population('mt'),
'mu' : pypopulation.get_population('mu'),
'mv' : pypopulation.get_population('mv'),
'mw' : pypopulation.get_population('mw'),
'mx' : pypopulation.get_population('mx'),
'my' : pypopulation.get_population('my'),
'mz' : pypopulation.get_population('mz'),
'na' : pypopulation.get_population('na'),
'ne' : pypopulation.get_population('ne'),
'ng' : pypopulation.get_population('ng'),
'ni' : pypopulation.get_population('ni'),
'nl' : pypopulation.get_population('nl'),
'no' : pypopulation.get_population('no'),
'np' : pypopulation.get_population('np'),
'nz' : pypopulation.get_population('nz'),
'om' : pypopulation.get_population('om'),
'pa' : pypopulation.get_population('pa'),
'pe' : pypopulation.get_population('pe'),
'pg' : pypopulation.get_population('pg'),
'ph' : pypopulation.get_population('ph'),
'pk' : pypopulation.get_population('pk'),
'pl' : pypopulation.get_population('pl'),
'pr' : pypopulation.get_population('pr'),
'ps' : pypopulation.get_population('ps'),
'pt' : pypopulation.get_population('pt'),
'py' : pypopulation.get_population('py'),
're' : pypopulation.get_population('re'),
'ro' : pypopulation.get_population('ro'),
'rs' : pypopulation.get_population('rs'),
'ru' : pypopulation.get_population('ru'),
'rw' : pypopulation.get_population('rw'),
'sa' : pypopulation.get_population('sa'),
'sc' : pypopulation.get_population('sc'),
'sd' : pypopulation.get_population('sd'),
'se' : pypopulation.get_population('se'),
'sg' : pypopulation.get_population('sg'),
'sh' : pypopulation.get_population('sh'),
'si' : pypopulation.get_population('si'),
'sk' : pypopulation.get_population('sk'),
'sl' : pypopulation.get_population('sl'),
'sm' : pypopulation.get_population('sm'),
'sn' : pypopulation.get_population('sn'),
'so' : pypopulation.get_population('so'),
'sr' : pypopulation.get_population('sr'),
'st' : pypopulation.get_population('st'),
'sv' : pypopulation.get_population('sv'),
'sy' : pypopulation.get_population('sy'),
'sz' : pypopulation.get_population('sz'),
'td' : pypopulation.get_population('td'),
'tg' : pypopulation.get_population('tg'),
'th' : pypopulation.get_population('th'),
'tj' : pypopulation.get_population('tj'),
'tl' : pypopulation.get_population('tl'),
'tm' : pypopulation.get_population('tm'),
'tn' : pypopulation.get_population('tn'),
'tr' : pypopulation.get_population('tr'),
'tw' : pypopulation.get_population('tw'),
'tz' : pypopulation.get_population('tz'),
'ua' : pypopulation.get_population('ua'),
'ug' : pypopulation.get_population('ug'),
'us' : pypopulation.get_population('us'),
'uy' : pypopulation.get_population('uy'),
'uz' : pypopulation.get_population('uz'),
'va' : pypopulation.get_population('va'),
've' : pypopulation.get_population('ve'),
'vn' : pypopulation.get_population('vn'),
'ye' : pypopulation.get_population('ye'),
'yt' : pypopulation.get_population('yt'),
'za' : pypopulation.get_population('za'),
'zm' : pypopulation.get_population('zm'),
'zw' : pypopulation.get_population('zw')
}) 

# save into the file 
worldmap.render_to_file('PopulationMap.svg') 

print("Success") 
print(pypopulation.get_population('ad'))
print(pypopulation.get_population('ae'))
print(pypopulation.get_population('af'))
print(pypopulation.get_population('al'))
print(pypopulation.get_population('am'))
print(pypopulation.get_population('ao'))
print(pypopulation.get_population('aq'))
print(pypopulation.get_population('ar'))
print(pypopulation.get_population('at'))
print(pypopulation.get_population('au'))
print(pypopulation.get_population('az'))
print(pypopulation.get_population('ba'))
print(pypopulation.get_population('bd'))
print(pypopulation.get_population('be'))
print(pypopulation.get_population('bf'))
print(pypopulation.get_population('bg'))
print(pypopulation.get_population('bh'))
print(pypopulation.get_population('bi'))
print(pypopulation.get_population('bj'))
print(pypopulation.get_population('bn'))
print(pypopulation.get_population('bo'))
print(pypopulation.get_population('br'))
print(pypopulation.get_population('bt'))
print(pypopulation.get_population('bw'))
print(pypopulation.get_population('by'))
print(pypopulation.get_population('bz'))
print(pypopulation.get_population('ca'))
print(pypopulation.get_population('cd'))
print(pypopulation.get_population('cf'))
print(pypopulation.get_population('cg'))
print(pypopulation.get_population('ch'))
print(pypopulation.get_population('ci'))
print(pypopulation.get_population('cl'))
print(pypopulation.get_population('cm'))
print(pypopulation.get_population('cn'))
print(pypopulation.get_population('co'))
print(pypopulation.get_population('cr'))
print(pypopulation.get_population('cu'))
print(pypopulation.get_population('cv'))
print(pypopulation.get_population('cy'))
print(pypopulation.get_population('cz'))
print(pypopulation.get_population('de'))
print(pypopulation.get_population('dj'))
print(pypopulation.get_population('dk'))
print(pypopulation.get_population('do'))
print(pypopulation.get_population('dz'))
print(pypopulation.get_population('ec'))
print(pypopulation.get_population('ee'))
print(pypopulation.get_population('eg'))
print(pypopulation.get_population('eh'))
print(pypopulation.get_population('er'))
print(pypopulation.get_population('es'))
print(pypopulation.get_population('et'))
print(pypopulation.get_population('fi'))
print(pypopulation.get_population('fr'))
print(pypopulation.get_population('ga'))
print(pypopulation.get_population('gb'))
print(pypopulation.get_population('ge'))
print(pypopulation.get_population('gf'))
print(pypopulation.get_population('gh'))
print(pypopulation.get_population('gl'))
print(pypopulation.get_population('gm'))
print(pypopulation.get_population('gn'))
print(pypopulation.get_population('gq'))
print(pypopulation.get_population('gr'))
print(pypopulation.get_population('gt'))
print(pypopulation.get_population('gu'))
print(pypopulation.get_population('gw'))
print(pypopulation.get_population('gy'))
print(pypopulation.get_population('hk'))
print(pypopulation.get_population('hn'))
print(pypopulation.get_population('hr'))
print(pypopulation.get_population('ht'))
print(pypopulation.get_population('hu'))
print(pypopulation.get_population('id'))
print(pypopulation.get_population('ie'))
print(pypopulation.get_population('il'))
print(pypopulation.get_population('in'))
print(pypopulation.get_population('iq'))
print(pypopulation.get_population('ir'))
print(pypopulation.get_population('is'))
print(pypopulation.get_population('it'))
print(pypopulation.get_population('jm'))
print(pypopulation.get_population('jo'))
print(pypopulation.get_population('jp'))
print(pypopulation.get_population('ke'))
print(pypopulation.get_population('kg'))
print(pypopulation.get_population('kh'))
print(pypopulation.get_population('kp'))
print(pypopulation.get_population('kw'))
print(pypopulation.get_population('kz'))
print(pypopulation.get_population('la'))
print(pypopulation.get_population('lb'))
print(pypopulation.get_population('li'))
print(pypopulation.get_population('lk'))
print(pypopulation.get_population('lr'))
print(pypopulation.get_population('ls'))
print(pypopulation.get_population('lt'))
print(pypopulation.get_population('lu'))
print(pypopulation.get_population('lv'))
print(pypopulation.get_population('ly'))
print(pypopulation.get_population('ma'))
print(pypopulation.get_population('mc'))
print(pypopulation.get_population('md'))
print(pypopulation.get_population('me'))
print(pypopulation.get_population('mg'))
print(pypopulation.get_population('mk'))
print(pypopulation.get_population('ml'))
print(pypopulation.get_population('mm'))
print(pypopulation.get_population('mn'))
print(pypopulation.get_population('mo'))
print(pypopulation.get_population('mr'))
print(pypopulation.get_population('mt'))
print(pypopulation.get_population('mu'))
print(pypopulation.get_population('mv'))
print(pypopulation.get_population('mw'))
print(pypopulation.get_population('mx'))
print(pypopulation.get_population('my'))
print(pypopulation.get_population('mz'))
print(pypopulation.get_population('na'))
print(pypopulation.get_population('ne'))
print(pypopulation.get_population('ng'))
print(pypopulation.get_population('ni'))
print(pypopulation.get_population('nl'))
print(pypopulation.get_population('no'))
print(pypopulation.get_population('np'))
print(pypopulation.get_population('nz'))
print(pypopulation.get_population('om'))
print(pypopulation.get_population('pa'))
print(pypopulation.get_population('pe'))
print(pypopulation.get_population('pg'))
print(pypopulation.get_population('ph'))
print(pypopulation.get_population('pk'))
print(pypopulation.get_population('pl'))
print(pypopulation.get_population('pr'))
print(pypopulation.get_population('ps'))
print(pypopulation.get_population('pt'))
print(pypopulation.get_population('py'))
print(pypopulation.get_population('re'))
print(pypopulation.get_population('ro'))
print(pypopulation.get_population('rs'))
print(pypopulation.get_population('ru'))
print(pypopulation.get_population('rw'))
print(pypopulation.get_population('sa'))
print(pypopulation.get_population('sc'))
print(pypopulation.get_population('sd'))
print(pypopulation.get_population('se'))
print(pypopulation.get_population('sg'))
print(pypopulation.get_population('sh'))
print(pypopulation.get_population('si'))
print(pypopulation.get_population('sk'))
print(pypopulation.get_population('sl'))
print(pypopulation.get_population('sm'))
print(pypopulation.get_population('sn'))
print(pypopulation.get_population('so'))
print(pypopulation.get_population('sr'))
print(pypopulation.get_population('st'))
print(pypopulation.get_population('sv'))
print(pypopulation.get_population('sy'))
print(pypopulation.get_population('sz'))
print(pypopulation.get_population('td'))
print(pypopulation.get_population('tg'))
print(pypopulation.get_population('th'))
print(pypopulation.get_population('tj'))
print(pypopulation.get_population('tl'))
print(pypopulation.get_population('tm'))
print(pypopulation.get_population('tn'))
print(pypopulation.get_population('tr'))
print(pypopulation.get_population('tw'))
print(pypopulation.get_population('tz'))
print(pypopulation.get_population('ua'))
print(pypopulation.get_population('ug'))
print(pypopulation.get_population('us'))
print(pypopulation.get_population('uy'))
print(pypopulation.get_population('uz'))
print(pypopulation.get_population('va'))
print(pypopulation.get_population('ve'))
print(pypopulation.get_population('vn'))
print(pypopulation.get_population('ye'))
print(pypopulation.get_population('yt'))
print(pypopulation.get_population('za'))
print(pypopulation.get_population('zm'))
print(pypopulation.get_population('zw'))