-- дропаем таблицу texts вместе с идентификаторами и связями

drop table if exists 
public.texsts, 
public.words_row_count,
public.words_count,
public.m_names
cascade;

--Создаем таблицу

create table texts (
id integer primary key generated always as identity,
text_row text
);

-- наполняем тестовыми данными. Текст сгенерирован через lorem.paagraph()

INSERT INTO texts(text_row) VALUES
('Consectetur non dolor porro. Porro consectetur sit consectetur. Etincidunt tempora modi dolore aliquam. Magnam modi aliquam voluptatem tempora sit. Eius porro dolore adipisci. Etincidunt ipsum eius aliquam numquam eius. Porro ut neque magnam sed velit dolor numquam.') ,
('Sed dolorem velit adipisci tempora adipisci eius consectetur. Porro ut eius aliquam tempora quisquam voluptatem amet. Neque labore est voluptatem tempora amet. Amet eius non non quaerat amet neque dolor. Porro etincidunt amet aliquam est dolorem. Dolorem dolore neque tempora numquam adipisci tempora consectetur. Dolorem voluptatem quiquia sed quaerat. Modi voluptatem aliquam adipisci. Sed ut consectetur numquam ut dolor.') ,
('Sit ipsum sit modi neque amet. Quiquia sit amet sit velit dolorem. Quaerat quisquam porro est velit ipsum. Tempora quiquia neque adipisci. Adipisci dolorem labore eius. Dolor quiquia quiquia adipisci sed quisquam voluptatem. Ipsum etincidunt dolor eius magnam.') ,
('Porro dolorem quisquam dolor amet labore. Adipisci neque neque sit. Ut quisquam voluptatem etincidunt dolorem. Neque consectetur quaerat consectetur. Dolor dolorem voluptatem quisquam non adipisci. Porro dolor ut adipisci quisquam velit dolorem velit.') ,
('Sit amet dolorem dolore. Dolore sit dolorem dolore. Voluptatem neque neque ut sed. Modi quisquam voluptatem velit. Velit consectetur modi ipsum aliquam velit adipisci velit. Quiquia modi dolore amet est quaerat ipsum ipsum.') ,
('Non est dolor numquam velit quisquam ipsum quiquia. Numquam magnam quiquia porro. Neque magnam voluptatem dolorem aliquam voluptatem. Voluptatem ipsum numquam dolor ut. Amet numquam quaerat non. Voluptatem sed sed sit adipisci. Quiquia sed sit numquam consectetur. Aliquam consectetur ut labore non tempora velit tempora. Ut adipisci porro ut quiquia. Amet aliquam ipsum modi.') ,
('Neque dolore etincidunt dolore. Aliquam voluptatem labore consectetur consectetur labore magnam non. Dolorem magnam adipisci consectetur dolore est modi non. Porro numquam adipisci tempora. Magnam dolore tempora labore labore sit. Est dolore eius ut dolor. Non consectetur velit tempora dolore quaerat eius.') ,
('Adipisci dolor aliquam amet quaerat numquam numquam sit. Magnam adipisci non voluptatem sed eius quisquam. Dolore porro ipsum ipsum quiquia modi numquam dolore. Dolore quiquia quisquam numquam eius labore. Magnam ipsum modi adipisci.') ,
('Quaerat dolor consectetur neque tempora. Modi voluptatem voluptatem tempora est dolor sit. Velit etincidunt etincidunt quiquia velit. Ipsum ipsum ut velit numquam velit consectetur ipsum. Ut quaerat amet dolore quiquia quaerat ipsum non. Dolor neque porro dolor dolore sed etincidunt voluptatem. Velit velit quaerat numquam quiquia velit. Sed adipisci ut tempora eius quisquam.') ,
('Velit consectetur magnam porro velit dolor. Ipsum quisquam voluptatem dolorem sed ipsum. Sed dolor porro ut. Est quisquam tempora dolor quiquia etincidunt modi. Dolore non ut eius. Dolor porro tempora voluptatem. Etincidunt neque ut dolorem. Numquam ipsum non modi magnam.') ,
('Non tempora eius non ut etincidunt. Ut dolore etincidunt quisquam dolor. Quaerat porro dolore est dolorem eius. Est tempora adipisci numquam dolorem ut non dolorem. Sit voluptatem ipsum dolorem modi. Quisquam sed magnam non sed eius magnam. Eius aliquam tempora voluptatem magnam porro dolorem. Porro eius quisquam consectetur aliquam labore consectetur. Est etincidunt quaerat quisquam.') ,
('Aliquam numquam non amet ut. Quaerat est quiquia numquam velit ipsum dolore. Ut sit dolorem adipisci dolorem quiquia. Sed quisquam dolore velit numquam. Ut tempora ipsum adipisci non porro sit. Labore etincidunt porro sed voluptatem quaerat.') ,
('Dolorem labore dolor porro porro ut. Dolorem etincidunt ut neque. Magnam quiquia quiquia sed neque quisquam. Voluptatem non quaerat magnam voluptatem sed dolore. Sed dolore velit est magnam quisquam.') ,
('Quaerat consectetur sed numquam numquam voluptatem quiquia. Dolor eius velit quaerat labore quaerat sed porro. Consectetur dolor est tempora velit. Quisquam amet porro modi aliquam dolore tempora sit. Labore amet neque aliquam. Dolor quiquia sit dolor tempora. Ut magnam sit sed quaerat quiquia numquam. Magnam quaerat dolorem etincidunt ipsum eius. Magnam consectetur amet sed. Amet quaerat ipsum numquam ipsum ut.');

-- Считаем слова: слова отделены пробелами - нужно посчитать количество пробелов + 1 последнее слово

--create table words_row_count as

select *, length(trim(text_row)) - length(trim(replace(text_row,' ','')))+1 as words_count from texts

-- Находим слова встречающиеся чаще 10 раз

--create table words_count as 

select words,count(*) from
(
select string_to_table(lower(trim(replace(replace(text_row,'.',''),',',''))),' ') words from texts
)
group by words
having count(*)>10
order by count(*);

-- вычисление средней длины слов в строке

select id, 
	length(trim(replace(replace(replace(text_row,'.',''),',',''),' ','')))/(
	length(trim(replace(replace(text_row,'.',''),',','')))-length(trim(replace(replace(replace(text_row,'.',''),',',''),' ','')))
	)
from texts 

-- создадим таблицу и заполним данными
create table m_names 
(id integer unique not null primary key,
name varchar(50) )

insert into m_names (id,name) values
(1,'Алексей'),
(2,'Иван'),
(3,'Михаил'),
(4,'Антон'),
(5,'Василий'),
(6,'Иван')

-- ранг по алфавиту

select id,name, rank() over (order by name) as ABC_rank from m_names

-- запрос разделяет полное имя вида "фамилия, имя" на столбцы имя и фамилия и приводит формату "с большой буквы" :)
-- выполняется на тестовой строке, имена полей и таблица закомментированы

--'Smith, John'
select 
	'Smith, John' as 
	full_name,
	initcap(trim(lower(substr(
		'Smith, John'
		--full_name
		,position(' ' in
			'Smith, John'
			--full_name
			)+1)))) as name ,
	initcap(lower(left(
		'Smith, John'
		--full_name
		,position(', ' in 
			'Smith, John'
			--full_name
			)-1))) as surname
--from m_names
