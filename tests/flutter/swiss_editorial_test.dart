import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import '../lib/swiss_editorial.dart';

void main() {
  testWidgets('filter search and reset compose', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: SwissEditorialExample()));
    expect(find.text('3 stories / 0 saved'), findsOneWidget);
    await tester.tap(find.widgetWithText(FilterChip, 'Culture'));
    await tester.pumpAndSettle();
    expect(find.text('1 story / 0 saved'), findsOneWidget);
    await tester.enterText(find.byType(TextField), 'grid');
    await tester.pumpAndSettle();
    expect(find.text('No stories found'), findsOneWidget);
    await tester.ensureVisible(find.text('Reset filters'));
    await tester.tap(find.text('Reset filters'));
    await tester.pumpAndSettle();
    expect(find.text('3 stories / 0 saved'), findsOneWidget);
  });

  testWidgets('bookmark survives category changes and can be removed', (tester) async {
    tester.view.physicalSize = const Size(1024, 2400);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(const MaterialApp(home: SwissEditorialExample()));
    final save = find.text('+ Save: Less noise. More meaning.');
    await tester.ensureVisible(save);
    await tester.tap(save);
    await tester.pumpAndSettle();
    expect(find.text('3 stories / 1 saved'), findsOneWidget);
    await tester.ensureVisible(find.widgetWithText(FilterChip, 'Culture'));
    await tester.tap(find.widgetWithText(FilterChip, 'Culture'));
    await tester.pumpAndSettle();
    await tester.tap(find.widgetWithText(FilterChip, 'All'));
    await tester.pumpAndSettle();
    final saved = find.text('✓ Saved: Less noise. More meaning.');
    await tester.ensureVisible(saved);
    await tester.tap(saved);
    await tester.pumpAndSettle();
    expect(find.text('3 stories / 0 saved'), findsOneWidget);
  });

  testWidgets('compact large text dark theme has no layout exception', (tester) async {
    tester.view.physicalSize = const Size(375, 900);
    tester.view.devicePixelRatio = 1;
    addTearDown(tester.view.resetPhysicalSize);
    addTearDown(tester.view.resetDevicePixelRatio);
    await tester.pumpWidget(MaterialApp(
      theme: ThemeData.dark(),
      builder: (context, child) => MediaQuery(data: MediaQuery.of(context).copyWith(textScaler: const TextScaler.linear(2)), child: child!),
      home: const SwissEditorialExample(),
    ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    await tester.drag(find.byType(ListView), const Offset(0, -1200));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
  });
}
