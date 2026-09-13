import 'package:flutter/material.dart';

class NeoButton extends StatelessWidget {
  const NeoButton({super.key, this.onPressed});

  final VoidCallback? onPressed;

  @override
  Widget build(BuildContext context) {
    const ink = Color(0xFF0A0A0A);
    const accent = Color(0xFFFFDC58);

    return DecoratedBox(
      decoration: const BoxDecoration(
        color: accent,
        border: Border.fromBorderSide(BorderSide(color: ink, width: 2)),
        boxShadow: [BoxShadow(color: ink, offset: Offset(4, 4))],
      ),
      child: FilledButton(
        onPressed: onPressed,
        style: FilledButton.styleFrom(
          backgroundColor: accent,
          foregroundColor: ink,
          elevation: 0,
          minimumSize: const Size(44, 44),
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
          shape: const RoundedRectangleBorder(borderRadius: BorderRadius.zero),
        ),
        child: const Text('Publish', style: TextStyle(fontWeight: FontWeight.w800)),
      ),
    );
  }
}

class NeoCard extends StatelessWidget {
  const NeoCard({super.key, required this.title, this.child});

  final String title;
  final Widget? child;

  @override
  Widget build(BuildContext context) {
    const ink = Color(0xFF0A0A0A);
    return DecoratedBox(
      decoration: const BoxDecoration(
        color: Colors.white,
        border: Border.fromBorderSide(BorderSide(color: ink, width: 3)),
        boxShadow: [BoxShadow(color: ink, offset: Offset(8, 8))],
      ),
      child: Padding(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(title, style: const TextStyle(fontWeight: FontWeight.w800)),
            if (child != null) ...[const SizedBox(height: 12), child!],
          ],
        ),
      ),
    );
  }
}
